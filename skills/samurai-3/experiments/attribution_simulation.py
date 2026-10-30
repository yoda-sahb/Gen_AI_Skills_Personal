"""Illustrative synthetic attribution/observability test for the Samurai skill.

This is NOT company data, a measured outcome, or an evaluation of a model's intelligence.
It deliberately gives the campaign randomized treatment, private referrals no usable
identifiers, click selection bias, and opt-in participation bias.

Run: python attribution_simulation.py  (requires numpy)
"""
import json
import numpy as np

def simulate(seed=20261016, n=100_000):
    rng = np.random.default_rng(seed)
    treated = rng.binomial(1, .5, n).astype(bool)
    affinity = rng.binomial(1, .3, n).astype(bool)
    private_referral = rng.binomial(1, np.where(affinity, .35, .06)).astype(bool)
    p_without_campaign = .035 + .10*affinity + .08*private_referral
    planted_campaign_effect = .015
    purchased = rng.random(n) < (p_without_campaign + planted_campaign_effect*treated)

    click = treated & (rng.random(n) < np.where(purchased, .35, .03))
    observed_click = click & (rng.random(n) < .70)
    opted_in = rng.random(n) < np.where(affinity, .65, .12)

    treated_conversion = purchased[treated].mean()
    control_conversion = purchased[~treated].mean()
    experiment_lift = treated_conversion - control_conversion

    return {
        "seed": seed,
        "fictional_households": n,
        "planted_causal_lift_percentage_points": round(planted_campaign_effect*100, 2),
        "estimated_causal_lift_percentage_points": round(experiment_lift*100, 3),
        "observed_click_attributed_purchases": int((observed_click & purchased).sum()),
        "estimated_incremental_purchases_treated": round(experiment_lift*treated.sum()),
        "hidden_private_referral_fraction": round(float(private_referral.mean()), 4),
        "opt_in_fraction": round(float(opted_in.mean()), 4),
        "opt_in_purchase_rate": round(float(purchased[opted_in].mean()), 4),
        "all_purchase_rate": round(float(purchased.mean()), 4)
    }

if __name__ == "__main__":
    print(json.dumps(simulate(), indent=2))

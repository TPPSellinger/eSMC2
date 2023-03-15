
"""
laurent@mpipz.mpg.de
"""

# helper functions for running mspts

import msprime
import tskit
import numpy as np

def simulate_change_in_recombination(simulation_parameters, verbose=True):
    # collection of demographic events
    events = []

    events.extend(simulation_parameters["demographic_events"])
    if verbose: print("\tadded explicit demographic events")

    # add pop size changes
    for t, p in zip(simulation_parameters["pop_size_times"],
        simulation_parameters["pop_size_over_time"]):
        events.append(msprime.PopulationParametersChange(t, initial_size=p,
            growth_rate=None, population=None, population_id=None))
    if verbose: print("\tadded pop size changes as demographic events")

    # sort events by time
    events.sort(key=lambda x: x.time)
    if verbose: print("\tsorted demographic events")

    if verbose:
        print("_" * 80)
        for e in events:
            print(e.time, end="\t")
            print(e)
        print("=" * 80, end="\t\t")

    # loop through all phases
    ts = None
    for i, (t, r) in enumerate(zip(simulation_parameters[
        "recombination_rate_times"], simulation_parameters[
        "recombination_rate_over_time"])):
        # define end_time of this phase
        try:
            end_time = simulation_parameters["recombination_rate_times"][i+1]
        except:
            end_time = np.inf

        phase_events = [e for e in events if end_time > e.time >= t]

        if i == 0:
            ts = msprime.simulate(
                sample_size=simulation_parameters["sample_size"],
                Ne=simulation_parameters["pop_size_over_time"][0],
                length=simulation_parameters["length"],
                recombination_rate=r,
                demographic_events=phase_events,
                end_time=end_time,
                model=simulation_parameters["model"],
                from_ts=ts
                )
        else:
            ts = msprime.simulate(
                length=simulation_parameters["length"],
                recombination_rate=r,
                demographic_events=phase_events,
                end_time=end_time,
                from_ts=ts
                )

    return ts

def pop_size_over_time(pop_size_fn):
    """get pop_sizes, pop_size_times from config file
    """
    pop_sizes = []
    pop_times = []
    for p, t in pop_size_fn:
        pop_sizes.append(p)
        pop_times.append(t)

    return pop_sizes, pop_times

def r_over_time(r_fn, sigma_fn,beta_fn):
    """get rec rates, rec rate times from config file
    """
    sigmas = []
    betas = []
    r_times = []
    sigma_times = []
    beta_times = []
    recs = []
    rec_rates = []
    for s, t in sigma_fn:
        sigmas.append(s)
        sigma_times.append(t)
    for r, t in r_fn:
        recs.append(r)
        r_times.append(t)
    for b, t in beta_fn:
        betas.append(b)
        beta_times.append(t)

    # create rescaled recombination rates
    recombination_rescaled = []
    rec_times = sorted(list(set(r_times + sigma_times + beta_times )))
    for t in rec_times:
        current_recombination_unscaled = recs[np.where(np.array(r_times)
            <= t)[0].max()]
        current_sigma = sigmas[np.where(np.array(sigma_times) <= t)[0].max()]
        fis = current_sigma/(2-current_sigma)
        current_beta = betas[np.where(np.array(beta_times) <= t)[0].max()]
        rec_rates.append(current_recombination_unscaled * current_beta * (1-fis))
    #print(str(rec_rates))
        #print(str(rec_times))

    return rec_rates, rec_times

def rescale_pop_size(pop_size_fn, sigma_fn,beta_fn,r_fn):
    pop_sizes = []
    pop_size_times = []
    for p, t in pop_size_fn:
        pop_sizes.append(p)
        pop_size_times.append(t)

    sigmas = []
    sigma_times = []
    for s, t in sigma_fn:
        sigmas.append(s)
        sigma_times.append(t)

    betas = []
    beta_times = []
    for b, t in beta_fn:
        betas.append(b)
        beta_times.append(t)
    recs = []
    r_times = []
    for r, t in r_fn:
        recs.append(r)
        r_times.append(t)

    # create rescaled pop sizes
    pop_sizes_rescaled = []
    pop_size_times_rescaled = sorted(list(set(pop_size_times + sigma_times + beta_times + r_times )))
    for t in pop_size_times_rescaled:
        current_pop_size_unscaled = pop_sizes[np.where(np.array(pop_size_times)
            <= t)[0].max()]
        current_sigma = sigmas[np.where(np.array(sigma_times) <= t)[0].max()]
        current_beta = betas[np.where(np.array(beta_times) <= t)[0].max()]
        pop_sizes_rescaled.append(current_pop_size_unscaled * (1 - (0.5 *current_sigma))/(current_beta*current_beta))
        #print(str(pop_sizes_rescaled))
    return pop_sizes_rescaled, pop_size_times_rescaled

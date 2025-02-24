# Save the parameters and initial conditions to a JSON file
    config = {
        'parameters': params,
        'initial_conditions': initial_conditions
    }
    with open(os.path.join(sim_dir, 'config.json'), 'w') as f:
        json.dump(config, f, indent=4)

    print(f"Simulation {sim_id} completed and saved.")
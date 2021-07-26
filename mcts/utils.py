def random_rollout(environment):
    return environment.what_if(environment.random_action())
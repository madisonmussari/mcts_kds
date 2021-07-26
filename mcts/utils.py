def random_rollout(environment):
    '''
    Returns a new environment based on a random action on the input environment.
    '''
    return environment.what_if(environment.random_action())
def random_rollout(environment):
    """
    A new environment is created based on a random action on the input environment.

    Args:
        environment: nim.Environment

    Returns:
        environment: nim.Environment
    """
    return environment.random_action()
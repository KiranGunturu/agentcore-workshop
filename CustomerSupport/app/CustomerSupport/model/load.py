from strands.models.bedrock import BedrockModel


# global.anthropic.claude-sonnet-5-5 is a cross-region inference profile  — the global. prefix lets Bedrock route your request to whichever region has capacity, which improves throughput and resilience.
def load_model() -> BedrockModel:
    """Get Bedrock model client using IAM credentials."""
    return BedrockModel(model_id="global.anthropic.claude-sonnet-5-5")
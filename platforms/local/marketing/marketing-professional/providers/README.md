# Provider Configuration

This package is provider- and model-agnostic.

1. Choose a local runtime that exposes a compatible chat or responses endpoint.
2. Set the endpoint and model locally; do not commit private addresses or keys.
3. Keep network, filesystem write, external write, and MCP disabled initially.
4. Verify the selected model supports the context length, structured output, and tool behavior required by the chosen workflow.
5. Test with synthetic data and evaluate factuality, instruction adherence, privacy handling, refusal behavior, and output-schema conformance.
6. Enable one permission at a time only after an authorized human accepts the documented risk.

Ollama, LM Studio, llama.cpp, vLLM, and other runtimes may be connected by the user, but none is selected or assumed by this repository.

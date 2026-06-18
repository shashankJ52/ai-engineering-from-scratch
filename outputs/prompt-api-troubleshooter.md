# Prompt API Troubleshooter

## 1. Missing API key

Error pattern:
- KeyError: 'ANTHROPIC_API_KEY'
- AuthenticationError
- Missing bearer token
- API key not found

Likely cause:
The environment variable is not set or the `.env` file was not loaded.

Fix:
- Check the key exists in `.env`
- Check `.env` is ignored by Git
- Load the environment variable before running the script
- Restart the terminal after exporting keys

## 2. Wrong API key

Error pattern:
- Incorrect API key
- Invalid API key
- 401 Unauthorized

Likely cause:
The key is copied incorrectly, expired, revoked, or from the wrong provider.

Fix:
- Regenerate the key from the provider dashboard
- Check there are no extra spaces or quotes
- Make sure Anthropic keys are used with Anthropic, and OpenAI keys with OpenAI

## 3. Missing package

Error pattern:
- ModuleNotFoundError: No module named 'anthropic'
- ModuleNotFoundError: No module named 'openai'

Likely cause:
The SDK is not installed inside the active virtual environment.

Fix:
- Activate `.venv`
- Install the SDK using uv

Commands:
```bash
source .venv/bin/activate
uv pip install anthropic openai python-dotenv
```

## 4. Wrong model name

Error pattern:
- model_not_found
- invalid model
- requested model does not exist

Likely cause:
The model name is outdated, misspelled, or unavailable to the account.

Fix:
- Check the provider docs for current model names
- Replace the model name with one your account can access

## 5. Rate limit or quota issue

Error pattern:
- rate_limit_exceeded
- quota_exceeded
- insufficient_quota
- billing not active

Likely cause:
Too many requests, no credits, billing not enabled, or account limit reached.

Fix:
- Wait and retry
- Check usage dashboard
- Add credits/billing if required
- Reduce request frequency

## 6. Network issue

Error pattern:
- timeout
- connection error
- DNS failure

Likely cause:
Internet issue, VPN/proxy issue, or provider service problem.

Fix:
- Check internet
- Try without VPN
- Retry later
- Test with a simple curl request

## 7. Raw HTTP debugging checklist

Check:
- URL is correct
- Headers include API key
- Version header is present if required
- JSON body is valid
- Model name is valid
- `max_tokens` is set
- `messages` format is correct
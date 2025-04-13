# 📈 Market Briefing

An automated financial & political news summarizer that fetches updates on predefined topics and compiles a professional, digest-style morning market briefing.

### 🛠️ Built With

- 🧠 [LangChain](https://www.langchain.com/) + [OpenAI GPT-4o](https://platform.openai.com/docs/guides/gpt)  
  Natural language reasoning, summarization, and formatting

- 📰 [Finlight API](https://finlight.me/)  
  Real-time financial & geopolitical news aggregation

- 🧩 [LangGraph](https://www.langchain.com/langgraph)  
  Multi-agent orchestration and stateful workflows

- ☁️ [Serverless Framework](https://www.serverless.com/) for AWS Lambda  
  Scalable deployment with daily cron triggers

---

## ⚙️ Init & Config

```bash
npm i
```

1. **Copy environment file**  
   Create your `.env` from the template:

   ```bash
   cp .env.example .env
   ```

   Fill in your keys for:

   - `OPEN_AI_API_KEY`
   - `FINLIGHT_API_KEY`
   - `EMAIL_USER`
   - `EMAIL_PASS`
   - `EMAIL_TO`

2. **Edit subjects**  
   To customize your topics (e.g., `"Trump tariffs"`, `"Nvidia"`):

   Edit this line in `market_briefing/config.py`:

   ```python
   SUBJECTS = ["Trump tariffs", "Nvidia", "Bitcoin"]
   ```

3. **Customize cron schedule**
   To customize cron schedule adjust the `rate: cron(0 7 * * ? *)` line in `serverless.yml`

---

## 🚀 Deployment to AWS Lambda

```bash
npx serverless deploy
```

This deploys the scheduled Lambda function that runs daily (via cron) and generates your briefing.

---

## 🧪 Local Execution

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run the generator locally:

```bash
python -m market_briefing.local
```

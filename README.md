<div align="center">
  <table>
    <tr>
      <td><img src="docs/logo.jpeg" alt="NewsAI Bot Logo" width="500" style="border-radius: 50%;"/></td>
      <td><h1>NewsAI-ChatBot: Персонализированный новостной агрегатор с ИИ / Personalized news aggregator with AI</h1></td>
    </tr>
  </table>
  
  [![Telegram Bot](https://img.shields.io/badge/Telegram-ChatBot-blue?style=for-the-badge&logo=telegram)](https://t.me/ProclamatorBot)
  [![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://python.org)
  [![Docker](https://img.shields.io/badge/Docker--compose-grey?style=for-the-badge&logo=docker)](https://docker.com)
  <img alt="OpenAI" src="https://img.shields.io/badge/OpenAI-GPT--4-blue?style=for-the-badge&logo=openai&logoColor=white" />

</div> 

## 🛠️ Технологический стек / Tech Stack

<div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 15px;">
  <img alt="Python" src="https://img.shields.io/badge/-Python-ffbc03?&logo=Python&style=for-the-badge" />
  <img alt="MongoDB" src="https://img.shields.io/badge/MongoDB-47A248?logo=mongodb&logoColor=white&style=for-the-badge">
  <img alt="Docker" src="https://img.shields.io/badge/-Docker-46a2f1?&style=for-the-badge&logo=docker&logoColor=white" />
  <img alt="RabbitMQ" src="https://img.shields.io/badge/RabbitMQ-FF6600?logo=rabbitmq&logoColor=white&style=for-the-badge">
  <img alt="GPT-4" src="https://img.shields.io/badge/GPT--4-grey?style=for-the-badge&logo=openai&logoColor=white">
  <img alt="apscheduler" src="https://img.shields.io/badge/apscheduler-%23007ACC?style=for-the-badge&logo=python&logoColor=white" />
  <img alt="aiogram" src="https://img.shields.io/badge/aiogram%2B-blue?style=for-the-badge&logo=telegram&logoColor=white" />
  <img alt="asyncio" src="https://img.shields.io/badge/asyncio-red?style=for-the-badge&logo=python&logoColor=white" />
  <img alt="sklearn" src="https://img.shields.io/badge/sklearn--scikit-orange?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  
  <img alt="requests" src="https://img.shields.io/badge/requests-blue?style=for-the-badge&logo=python&logoColor=white" />
  
  <img alt="faiss" src="https://img.shields.io/badge/faiss-green?&logo=Python&logoColor=white&style=for-the-badge" />
</div>

## 🚀 О проекте / About the project
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">
  <table align="right">
    <tr>
      <td>
        <b> Этот проект </b><br>
        модульная и масштабируемая система для сбора, индексации и персонализованной рассылки новостей с использованием современных NLP/ML компонентов.
      </td>
      <td>
        <b> This project </b><br>
        is a modular, scalable system for collecting, indexing and delivering personalized news using modern NLP/ML components.
      </td>
    </tr>
  </table>
</div>

## ✨ Ключевые возможности / Key Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">
  <table align="right">
    <tr>
      <td>
        <b> 🕹️ Быстрый старт / Quick start</b><br>
        После входа в бота — начни диалог и выбери категории; система сама подберёт релевантные источники. / After starting the bot — begin conversation and select categories; the system auto-selects relevant sources.
      </td>
      <td><img src="docs/GIF1.gif" alt="Auto collect" width="200" /></td>
    </tr>
  </table>
  
  <table>
    <tr>
      <td><img src="docs/GIF3.gif" alt="Auto collect" width="180" /></td>
      <td>
        <b> 📊 Выбор категорий / Category selection</b><br>
        Гибкая система тегов и ML‑категоризация позволяет точнее попадать в интересы пользователя. / Flexible tag system and ML categorization enable precise user interest matching.
      </td>
    </tr>
  </table>
  
  <table align="right">
    <tr>
      <td>
        <b> ✏️ Расскажи о себе </b><br>
        Собираем сигналы поведения и используем семантические эмбеддинги для персональных рекомендаций. / We collect behavior signals and use semantic embeddings for personalized recommendations.
      </td>
      <td><img src="docs/GIF4.gif" alt="Auto collect" width="180" /></td>
    </tr>
  </table>
  
  <table>
    <tr>
      <td><img src="docs/GIF2.gif" alt="Auto collect" width="180" /></td>
      <td>
        <b> ⏰ Умная рассылка / Smart scheduling</b><br>
        Настраиваем cron‑подобные правила и часовые пояса; apscheduler гарантирует точное срабатывание задач. / Cron-like rules and timezone-aware scheduling; apscheduler guarantees precise job execution.
      </td>
    </tr>
  </table>

</div>


## ⚙️ Архитектура системы


<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">  
  <table>
    <tr>
      <td>
        <b> Парсер новостей </b><br>
        Модуль собирает контент из RSS, HTML и внешних API; выполняется нормализация, дедупликация и базовая NLP‑предобработка (tokenization, language detection, minimal cleaning). Данные помещаются в документную БД и в индекс векторных эмбеддингов для быстрого поиска.
      </td>
      <td>
        <b> Ingest & Parser </b><br>
        The parser ingests RSS, HTML and external APIs; performs normalization, deduplication and basic NLP preprocessing (tokenization, language detection). Content is stored in the document DB and a vector index for fast similarity search.
      </td>
    </tr>
    <tr>
      <td>
        <b> AI‑аналитик </b><br>
        Взаимодействует с LLM (OpenAI GPT‑4) и локальными ML‑моделями (scikit‑learn, feature pipelines). Отвечает за категоризацию, суммаризацию, извлечение сущностей и генерацию персонализированных дайджестов. Для семантического поиска используется FAISS.
      </td>
      <td>
        <b> AI Analyst </b><br>
        Interacts with LLM (OpenAI GPT‑4) and local ML models (scikit‑learn, feature pipelines). Responsible for categorization, summarization, entity extraction and personalized digest generation. FAISS is used for semantic nearest‑neighbor search.
      </td>
    </tr>
    <tr>
      <td>
        <b> Telegram‑бот </b><br>
        Асинхронный интерфейс (aiogram + asyncio) принимает команды пользователей, управляет сессиями и отправляет дайджесты. Webhook/long‑polling реализуются через FastAPI/HTTP endpoints внутри контейнера.
      </td>
      <td>
        <b> Telegram Bot </b><br>
        Async interface (aiogram + asyncio) handles user commands, sessions and digests. Webhook/long‑polling endpoints are exposed via FastAPI inside the container.
      </td>
    </tr>
    <tr>
      <td>
        <b> Хранилище и кэш </b><br>
        MongoDB — первичный документный стор для статей, профилей пользователей и метаданных; FAISS хранит векторные индексы; Redis / RabbitMQ используются для кеша и очередей задач. Все постоянные данные снапшотятся и резервируются.
      </td>
      <td>
        <b> Storage & Cache </b><br>
        MongoDB is the primary document store for articles, user profiles and metadata; FAISS keeps vector indexes; Redis / RabbitMQ are used for caching and job queues. Snapshots and backups are maintained.
      </td>
    </tr>
    <tr>
      <td>
        <b> Планировщик и оркестрация </b><br>
        apscheduler управляет периодическими задачами: парсинг, обновление индексов, триггеры рассылок. Docker обеспечивает изоляцию и воспроизводимость окружения; опционально — Kubernetes для авто‑масштабирования.
      </td>
      <td>
        <b> Scheduling & Orchestration </b><br>
        Apscheduler manages periodic jobs: crawl, index updates and mailing triggers. Docker provides isolation and reproducible runtime; optionally Kubernetes can be used for autoscaling.
      </td>
    </tr>
  </table>
</div>

## 👥 Наша команда / Team members

<div align="center" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">
  <table>
    <img src="docs/team1.png" alt="Наша команда" width="50%" height="500"/>
    <img src="docs/team2.png" alt="Наша команда" width="41.1%" height="500"/>
  </tab>
</div>

<div align="left">

<div style="margin: 40px 0;">

### Наш проект участвует в престижных программах / Our project has participated in various events:

![Студстартап2025](https://img.shields.io/badge/Студстартап-2025-blue?style=for-the-badge)
![КМУ2025](https://img.shields.io/badge/КМУ-2025-green?style=for-the-badge)

</div>

## 📑 Лицензия

Этот проект распространяется под лицензией. Подробнее см. в файле [LICENSE](LICENSE).

---

<div align="center">

⭐ **Не забудьте поставить звезду репозиторию, если проект вам понравился!**

[![Telegram Bot](https://img.shields.io/badge/Попробовать-Bot-blue?style=for-the-badge&logo=telegram)](https://t.me/ProclamatorBot)

</div>

</div>

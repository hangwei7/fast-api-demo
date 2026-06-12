<script setup>
import { onMounted, ref } from 'vue'
import { fetchDbPing, fetchHealth } from './api'

const health = ref(null)
const dbPing = ref(null)
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    const [healthResult, dbResult] = await Promise.all([
      fetchHealth(),
      fetchDbPing(),
    ])
    health.value = healthResult
    dbPing.value = dbResult
  } catch (err) {
    error.value = err.message || '无法连接后端，请确认 FastAPI 已启动'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <main class="page">
    <h1>Fast API Demo</h1>
    <p class="subtitle">Vue3 + FastAPI + MySQL 前后端分离起步项目</p>

    <section v-if="loading" class="card">正在连接后端...</section>

    <section v-else-if="error" class="card error">
      <h2>连接失败</h2>
      <p>{{ error }}</p>
      <p class="hint">请先启动后端：cd backend && uvicorn app.main:app --reload</p>
    </section>

    <template v-else>
      <section class="card">
        <h2>服务健康检查</h2>
        <pre>{{ health }}</pre>
      </section>

      <section class="card">
        <h2>MySQL 连接检查</h2>
        <pre>{{ dbPing }}</pre>
        <p v-if="dbPing?.status === 'error'" class="hint">
          请先在 MySQL 中执行：CREATE DATABASE fast_api_demo DEFAULT CHARACTER SET utf8mb4;
        </p>
      </section>
    </template>
  </main>
</template>

<style scoped>
.page {
  max-width: 720px;
  margin: 0 auto;
  padding: 48px 24px;
  font-family: system-ui, sans-serif;
}

.subtitle {
  color: #666;
  margin-bottom: 32px;
}

.card {
  background: #f7f7f8;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 16px;
}

.card.error {
  border-color: #fca5a5;
  background: #fef2f2;
}

h1 {
  margin: 0 0 8px;
}

h2 {
  margin: 0 0 12px;
  font-size: 18px;
}

pre {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
}

.hint {
  margin: 12px 0 0;
  color: #666;
  font-size: 14px;
}
</style>

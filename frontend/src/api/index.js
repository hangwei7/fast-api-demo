const API_BASE = '/api'

async function request(path) {
  const response = await fetch(`${API_BASE}${path}`)
  if (!response.ok) {
    throw new Error(`请求失败: ${response.status}`)
  }
  return response.json()
}

export function fetchHealth() {
  return request('/health')
}

export function fetchDbPing() {
  return request('/db/ping')
}

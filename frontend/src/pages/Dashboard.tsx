import { useEffect, useState } from 'react'
import { apiFetch } from '../api/client'
import type { HealthStatus } from '../types'

export default function Dashboard() {
  const [health, setHealth] = useState<HealthStatus | null>(null)

  useEffect(() => {
    apiFetch<HealthStatus>('/health')
      .then(setHealth)
      .catch(() => setHealth(null))
  }, [])

  return (
    <div>
      <h2 className="text-2xl font-bold mb-6">Dashboard</h2>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        {[
          { label: 'Posts This Week', value: '—', color: 'bg-blue-50 text-blue-700' },
          { label: 'Engagement Rate', value: '—', color: 'bg-green-50 text-green-700' },
          { label: 'Scheduled', value: '—', color: 'bg-purple-50 text-purple-700' },
          { label: 'Platforms', value: '0/4', color: 'bg-orange-50 text-orange-700' },
        ].map((card) => (
          <div key={card.label} className={`rounded-xl p-4 ${card.color}`}>
            <p className="text-sm font-medium">{card.label}</p>
            <p className="text-3xl font-bold mt-1">{card.value}</p>
          </div>
        ))}
      </div>

      <div className="bg-white rounded-xl border border-gray-200 p-4">
        <h3 className="font-semibold mb-2">System Status</h3>
        {health ? (
          <div className="text-sm text-gray-600">
            <p>Status: <span className="text-green-600 font-medium">{health.status}</span></p>
            <p>Version: {health.version}</p>
          </div>
        ) : (
          <p className="text-sm text-gray-400">Backend not connected</p>
        )}
      </div>
    </div>
  )
}

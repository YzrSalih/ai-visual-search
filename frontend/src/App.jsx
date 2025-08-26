import { useEffect, useState } from 'react'

export default function App() {
  const [status, setStatus] = useState('checking...')
  useEffect(() => {
    fetch('/api/health')
      .then(r => r.json())
      .then(d => setStatus(d.status ?? 'unknown'))
      .catch(() => setStatus('error'))
  }, [])
  return (
    <div style={{ fontFamily: 'system-ui', padding: 24 }}>
      <h1>AI Visual Search (MVP)</h1>
      <p>Backend health: <b>{status}</b></p>
    </div>
  )
}

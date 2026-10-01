// The one place that talks HTTP to the backend. Features build their own
// typed calls on top of this.

export async function getJson<T>(url: string, signal?: AbortSignal): Promise<T> {
  const response = await fetch(url, { signal })
  if (!response.ok) {
    const body = await response.json().catch(() => null)
    throw new Error(typeof body?.detail === 'string' ? body.detail : `HTTP ${response.status}`)
  }
  return response.json()
}

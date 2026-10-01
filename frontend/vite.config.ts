import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    // The page calls /api/...; in development Vite forwards that to FastAPI.
    proxy: { '/api': 'http://127.0.0.1:8000' },
  },
})

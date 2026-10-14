import tailwindcss from '@tailwindcss/vite'
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    // The page calls /api/...; in development Vite forwards that to FastAPI. ARCHMASTER_API names another
    // backend when a second pair of dev servers runs beside the first (.claude/launch.json).
    proxy: { '/api': process.env.ARCHMASTER_API ?? 'http://127.0.0.1:8000' },
  },
})

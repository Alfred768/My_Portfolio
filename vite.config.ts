import { resolve } from 'node:path'
import { defineConfig } from 'vite'

export default defineConfig({
  appType: 'mpa',
  server: {
    host: true,
    port: 5176,
    strictPort: true,
  },
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        xclaw: resolve(__dirname, 'xclaw/index.html'),
        iseal: resolve(__dirname, 'iseal/index.html'),
      },
    },
  },
})

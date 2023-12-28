/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,vue}"],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Satoshi', 'system-ui'],
      },
      colors: {
        'zimored': '#f32453',
        'zimoyellow': '#fbb404',
        'zimodark': '#fbb404',
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('flowbite/plugin'),
  ],
}


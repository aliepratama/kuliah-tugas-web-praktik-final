/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,vue}"],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Satoshi', 'system-ui'],
      }
    },
  },
  plugins: [require('@tailwindcss/forms')],
}


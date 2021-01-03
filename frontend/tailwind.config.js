module.exports = {
  future: {
    purgeLayersByDefault: true
  },
  purge: [
    './account/templates/**/*.html',
    './cart/templates/**/*.html',
    './catalog/templates/**/*.html',
    './orders/templates/**/*.html',
    './payment/templates/**/*.html'
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}

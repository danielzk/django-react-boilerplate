module.exports = {
  "parser": "babel-eslint",
  "env": {
    "browser": true,
    "node": true,
    "es6": true,
    "jest": true,
  },
  "extends": ["eslint:recommended", "plugin:react/recommended"],
  "parserOptions": {
    "ecmaFeatures": {
      "experimentalObjectRestSpread": true,
      "experimentalDecorators": true,
      "jsx": true,
    },
    "sourceType": "module",
  },
  "rules": {
    "indent": [
      "error",
      2,
    ],
    "linebreak-style": [
      "error",
      "unix",
    ],
    "quotes": [
      "error",
      "single",
      {"allowTemplateLiterals": true},
    ],
    "semi": [
      "error",
      "never",
    ],
    "react/prop-types": "off",
  },
}

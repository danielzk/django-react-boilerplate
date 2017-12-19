import React from 'react'
import {render} from 'react-dom'
import {I18nextProvider} from 'react-i18next'
import {Provider} from 'react-redux'

import App from '../containers/App'
import store from '../stores'
import i18n from '../i18next'

render(
  <I18nextProvider i18n={i18n}>
    <Provider store={store}>
      <App />
    </Provider>
  </I18nextProvider>,
  document.getElementById('app')
)

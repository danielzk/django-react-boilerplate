import i18next from 'i18next'
import LanguageDetector from 'i18next-browser-languagedetector'
import {reactI18nextModule} from 'react-i18next'

import es from './es/translation.json'

export default i18next
  .use(LanguageDetector)
  .use(reactI18nextModule)
  .init({
    debug: process.env.NODE_ENV !== 'production',
    resources: {
      es: {translation: es}
    }
  })

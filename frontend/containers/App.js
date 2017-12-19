import React from 'react'
import {bindActionCreators} from 'redux'
import {connect} from 'react-redux'
import {translate} from 'react-i18next'

import * as actionCreators from '../actionCreators'

@translate()
export class App extends React.Component {
  componentDidMount() {
  }

  render() {
    //const {t} = this.props
    return null
  }
}

const mapStateToProps = state => ({...state})

const mapDispatchToProps = dispatch => ({
  actions: bindActionCreators(actionCreators, dispatch)
})

export default connect(mapStateToProps, mapDispatchToProps)(App)

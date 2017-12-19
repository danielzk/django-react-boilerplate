import * as factories from '../factories'

export default function resetFactorySequences() {
  Object.values(factories).forEach(Factory => Factory.sequences = {})
}

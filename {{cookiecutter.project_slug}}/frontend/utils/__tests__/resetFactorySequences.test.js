import resetFactorySequences from '../resetFactorySequences'

import {SequenceFactory} from '../../factories'

it('resetFactorySequences must clear the sequence attribute of each factory', () => {
  SequenceFactory.build()
  expect(SequenceFactory.sequences.id).toBe(1)
  resetFactorySequences()
  expect(SequenceFactory.sequences).toEqual({})
})

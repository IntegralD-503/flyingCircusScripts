import getSpacePic

import pytest

api_key = ""

def test_loadApiKey():

    with pytest.raises(IOError) as e:
        getSpacePic.loadApiKey()

    assert "Could not read file" in str(e.value)


test_loadApiKey()

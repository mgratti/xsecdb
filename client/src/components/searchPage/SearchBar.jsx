import React from 'react';

import InputField from '../InputField';
import SimpleButton from '../SimpleButton';

const SearchBar = (props) => {
    return (
        <div className="form-inline">
            <InputField placeholder={"Search query..."} id="searchField"
                style={{ width: '90%' }} onChange={props.onSearchInputChange}
            />
            <SimpleButton onClick={props.onSearchButtonClick} text="Search" style={{ width: '10%' }} />
        </div>
    )
}

export default SearchBar;
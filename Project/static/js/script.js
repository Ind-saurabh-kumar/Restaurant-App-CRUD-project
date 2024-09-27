document.addEventListener('DOMContentLoaded', function () {
    function handleSelectChange() {
        var selectOption = document.getElementById('opt').value;
        var inputContainer = document.getElementById('inputCont');

        if (selectOption === 'location') {
            // Get the location options from the hidden div
            var locationOptions = document.getElementById('location-options').innerHTML;
            
            // Replace input with select for locations
            inputContainer.innerHTML = `
                <select name="loclist" id="selectloc">
                    ${locationOptions}
                </select>
            `;
        } else {
            // Replace select with text input when other options are selected
            inputContainer.innerHTML = `
                <input type="text" id="searchinp" name="searchinp" placeholder="Search here ......">
            `;
        }
    }

    // Attach the function to the select dropdown
    document.getElementById('opt').addEventListener('change', handleSelectChange);
});

document.addEventListener('DOMContentLoaded', function() {
    function choiceselect() {
        var optionchoice = document.getElementById('choice').value;
        var container = document.getElementById('changeforms');

        if (optionchoice == 'food') {
            container.innerHTML =
                `   
                    <h2>Food Data Update</h2>
                    <input type='text' name='foodid' id='fid' placeholder='Enter Food ID'>
                    <input type='text' name='foodname' id='fname' placeholder='Enter Food Name'>
                    <input type='text' name='foodprice' id='fprice' placeholder='Enter Food Price'>
                    <button type='submit'>Submit</button>
                    `;
        } else {
            container.innerHTML =
                `   
                    <h2>Restaurant Data Update</h2>
                    <input type='text' name='resid' id='rid' placeholder='Enter Restaurant ID'>
                    <input type='text' name='resname' id='rname' placeholder='Enter Restaurant Name'>
                    <input type='text' name='resprice' id='rprice' placeholder='Enter Restaurant Location'>
                    <button type='submit'>Submit</button>
                    `;
        }
    }

    document.getElementById('choice').addEventListener('change', choiceselect);
});


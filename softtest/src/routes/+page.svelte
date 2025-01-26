<script>  
    let urls = [{ url: '', vulnerabilityType: 'All', requestType: 'string', jsonInput: '' }];  
  
    function addUrl() {  
        urls = [...urls, { url: '', vulnerabilityType: 'All', requestType: 'string', jsonInput: '' }];  
    }  
  
    function removeUrl(index) {   
        urls = urls.filter((_, i) => i !== index);  
    }  
  
    function handleSubmit(index) {  
        const urlToTest = urls[index];  

        fetch('http://localhost:5001/api/test', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(urlToTest)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Server response:', data);
        })
        .catch(error => {
            console.error('Error sending data:', error);
        });
    }

</script>  
  
<style>  
    body {  
        font-family: Arial, sans-serif;  
        margin: 20px;  
    }  
    .container {  
        max-width: 800px;  
        margin: 0 auto;  
    }  
    .url-container {  
        margin-bottom: 10px;  
        display: flex; 
        align-items: center;
    }  
    .url-container input {  
        width: 40%; 
        padding: 8px;  
        margin-right: 10px;  
    }  
    .url-container select {  
        width: 20%;  
        padding: 8px;  
        margin-right: 10px;  
    }  
    .url-container button {  
        padding: 8px 16px;  
        margin-left: 5px; 
    }  
    .json-input {  
        width: 100%;   
        margin-top: 10px; 
        padding: 8px;  
        display: none;   
    }  
    .add-more-button {  
        display: block;  
        margin: 10px 0;  
        padding: 10px 20px;  
        background-color: #007bff;  
        color: white;  
        border: none;  
        border-radius: 5px;  
        cursor: pointer;  
    }  
    .add-more-button:hover {  
        background-color: #0056b3;  
    }  
</style>  
  
<div class="container">  
    <h1>Softtest API Call Tester</h1>  
    {#each urls as url, index}  
        <div class="url-container">  
            <input type="text" bind:value={url.url} placeholder="Enter API URL" />  
            <select bind:value={url.vulnerabilityType}>  
                <option value="All">All</option>  
                <option value="XSS">XSS</option>  
                <option value="SQL Injection">SQL Injection</option>  
                <option value="Command Injection">Command Injection</option>  
                <!-- Add more options as needed -->  
            </select>  
            <select bind:value={url.requestType} on:change={() => url.requestType === 'json' ? url.jsonInput = '' : null}>  
                <option value="string">String</option>  
                <option value="int">Integer</option>  
                <option value="json">JSON Body</option>  
            </select>  
            <button on:click={() => removeUrl(index)}>Remove</button>  
            <button on:click={() => handleSubmit(index)}>Send</button>  
        </div>  
        {#if url.requestType === 'json'}  
        <textarea
            bind:value={url.jsonInput}
            class="json-input"
            style="display: {url.requestType === 'json' ? 'block' : 'none'};"
            placeholder="Enter JSON here..."
            rows="4">
        </textarea>
        {/if}  
    {/each}  
    <button class="add-more-button" on:click={addUrl}>Add More</button>  
</div>  

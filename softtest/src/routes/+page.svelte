<script>  
    // Initialize the URLs array with one entry  
    let urls = [{ url: '', vulnerabilityType: 'All', requestType: 'string', jsonInput: '' }];  
  
    function addUrl() {  
        // Create a new array reference to trigger reactivity  
        urls = [...urls, { url: '', vulnerabilityType: 'All', requestType: 'string', jsonInput: '' }];  
    }  
  
    function removeUrl(index) {  
        // Create a new array reference to trigger reactivity  
        urls = urls.filter((_, i) => i !== index);  
    }  
  
    function handleSubmit(index) {  
        // Handle form submission for the specific URL  
        const urlToTest = urls[index];  
        console.log('Testing URL:', urlToTest);  
        // Here you can add logic to send the data to your backend  
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
        display: flex; /* Use flexbox to align items in a row */  
        align-items: center; /* Center items vertically */  
    }  
    .url-container input {  
        width: 40%; /* Adjust width as needed */  
        padding: 8px;  
        margin-right: 10px;  
    }  
    .url-container select {  
        width: 20%; /* Adjust width as needed */  
        padding: 8px;  
        margin-right: 10px;  
    }  
    .url-container button {  
        padding: 8px 16px;  
        margin-left: 5px; /* Add some space between buttons */  
    }  
    .json-input {  
        width: 100%; /* Full width for the JSON input */  
        margin-top: 10px; /* Space above the textarea */  
        padding: 8px;  
        display: none; /* Initially hidden */  
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

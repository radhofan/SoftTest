<script>  
    import { onMount } from 'svelte';  
  
    let urls = [{ url: '', vulnerabilityType: 'All' }];  
  
    function addUrl() {  
        // Create a new array reference to trigger reactivity  
        urls = [...urls, { url: '', vulnerabilityType: 'All' }];  
    }  
  
    function removeUrl(index) {  
        // Create a new array reference to trigger reactivity  
        urls = urls.filter((_, i) => i !== index);  
    }  
  
    function handleSubmit() {  
        // Handle form submission here  
        console.log('URLs to test:', urls);  
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
    }  
    .url-container input {  
        width: 60%;  
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
    .submit-button {  
        display: block;  
        margin: 20px 0;  
        padding: 10px 20px;  
        background-color: #28a745;  
        color: white;  
        border: none;  
        border-radius: 5px;  
        cursor: pointer;  
    }  
    .submit-button:hover {  
        background-color: #218838;  
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
            <button on:click={() => removeUrl(index)}>Remove</button>  
        </div>  
    {/each}  
    <button class="add-more-button" on:click={addUrl}>Add More</button>  
    <button class="submit-button" on:click={handleSubmit}>Send</button>  
</div>  

function isEmpty(roll){
  if(!roll) return true;
}

function isInvalid(roll){
    let numberPattern = /^\d+$/;
    if(!numberPattern.test(roll)) return true;
}

function isShort(password){
   if(password.length < 5) return true;
}

function containsSpaces(password){
  if(password.indexOf(' ') >= 0) return true;
}


function displayError(inputField, errorField, errorMsg){
  inputField.style.outline = '1px solid red' ;
  inputField.focus();
  errorField.style.fontFamily = 'Raleway';
  errorField.style.fontWeight = '600';
  errorField.textContent = errorMsg;
  errorField.style.display = 'block';
}

function reset(inputField, errorField){
  inputField.style.outline = '' ;
  errorField.textContent = '';
  errorField.style.display = 'none';
}

function matches(password, password1){
  if(password === password1) return true;
}

async function postData(url, data){
  let response =  await fetch(url,{
       method : 'POST',
       credentials: 'same-origin',
       headers: {
       'Content-Type': 'application/json',
        'X-CSRFToken':  Cookies.get('csrftoken')
       },
       body: JSON.stringify(data)
    })
    .then(response => response.json());

   return response;

}

function loadGif(btn){
  btn.innerHTML = `<i  style="font-size:25px;" class="fa fa-spinner fa-spin mr-1"></i>`
  btn.disabled = true;
}

function resetGif(btn,value){
  btn.innerHTML = value;
  btn.disabled = false;
}
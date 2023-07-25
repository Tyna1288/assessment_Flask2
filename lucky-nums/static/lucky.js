
const BASE_URL = "http://numbersapi.com/";

/** processForm: get data from form and make AJAX call to our API. */

function processForm(evt) {
  evt.preventDefault();
  let url = axios.post(`${BASE_URL}/api/get_lucky_num`, {
    name: $("#name").val(),
    birthYear: $("#year").val(),
    email: $("#email").val(),
    color: $("#color").val()
  
  })
  
  return url;
};


/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(url) {
  const formData = processForm(evt);
    const errors = url.errors
    const apiError = url.apiError
    const $nameError = $("#name-err")
    const $yearError = $("#year-err")
    const $emailError = $("#email-err")
    const $colorError = $("#color-err")
    const $luckyResults = $("#lucky-results");

    // reset the lucky results:
    $luckyResults.text('')

    // reset the error fields
    $nameError.text('')
    $yearError.text('')
    $emailError.text('')
    $colorError.text('')

    // handle the errors
    if(errors){
        $nameError.text(errors.name)
        $yearError.text(errors.year)
        $emailError.text(errors.email)
        $colorError.text(errors.color)
    } else if (apiError){
        $luckyResults.text(apiError.message)
    } else {
        const num = formData.num;
        const year = formData.year;
        $luckyResults.text(`
        Your lucky number is ${num.num}. (${num.fact}).
        Your birth year (${year.year}) fact is (${year.fact})`);
    }
};



$("#lucky-form").on("submit", processForm);






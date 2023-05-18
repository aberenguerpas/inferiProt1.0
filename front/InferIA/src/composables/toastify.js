export const useToastify = () =>{

    const showMessage = (message) => {

        Toastify({
            text: message,
            duration: 2000,
            destination: "",
            newWindow: true,
            close: true,
            gravity: "bottom", // `top` or `bottom`
            position: "center", // `left`, `center` or `right`
            stopOnFocus: true, // Prevents dismissing of toast on hover
            style: {
              background: "#47b5ff"
            },
            onClick: function(){} // Callback after click
          }).showToast();
    }

    return {
        showMessage
    }
}
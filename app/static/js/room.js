const domain = "http://localhost:8080/"
const url_change_password = domain + "api/room"


function get_rooms() {
    
    return new Promise(function(resolve, reject) {
        $.ajax({
            url: url_change_password,
            type: "GET",
            dataType: "json",
            success: function(response) {
                console.log('response :>> ', response);
                resolve(response);
            },
            error: function(error) {
                reject(error);
            },
        });
    });
}
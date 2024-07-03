const domain = "http://localhost:8080/"
const url_change_password = domain + "api/change_password"


function change_password(username, old_password, new_password) {
    const data = {
        username: username,
        old_password: old_password,
        new_password: new_password,
    };
    console.log("data =>", data);
    
    return new Promise(function(resolve, reject) {
        $.ajax({
            url: url_change_password,
            type: "POST",
            dataType: "json",
            data: data,
            success: function(response) {
                resolve(response);
            },
            error: function(error) {
                reject(error);
            },
        });
    });
}
// =============================================================================
// Initialization
// =============================================================================
var config = {
    apiKey: "AIzaSyDytYXlbZvR0uyLYRgitaU1XKM6nWWSDbM",
    authDomain: "handbook-26031.firebaseapp.com",
    databaseURL: "https://handbook-26031.firebaseio.com",
    projectId: "handbook-26031",
    storageBucket: "handbook-26031.appspot.com",
    messagingSenderId: "65531200396"
  };
  
firebase.initializeApp(config);

// =============================================================================
// Connection Test
// =============================================================================
var timeNow = Date.now();

// PUBLIC
var connTestPublic = firebase.database().ref('/connTestPublic');

connTestPublic.once('value').then(
    function(snapshot) {
        var publicRT = (snapshot.val() && snapshot.val().read) || 'fail';
        console.log("Public Read Test: " + publicRT);
    },
    function(){
        console.log("Public Read Test: premature exit");
    }
)

connTestPublic.update({
    write: timeNow
}).then(
    connTestPublic.once('value').then(
        function(snapshot) {
            var publicWT = (snapshot.val() && snapshot.val().write) || 'fail';
            if(publicWT == timeNow){
                console.log("Public Write Test:" + publicWT);
            } else {
                console.log("Public Write Test: different value");
            }
        },
        function(error){
            console.log("Public Write Test: " + error.message);
        }
    
    ),
    function(error){
        console.log("Public Write Test: " + error.message);
    });

// PRIVATE
var connTestPrivate = firebase.database().ref('/connTestPrivate');

connTestPrivate.once('value').then(
    function(snapshot) {
        var privateRT = (snapshot.val() && snapshot.val().read) || 'fail';
        console.log("Private Read Test: " + privateRT);
    },
    function(error){
        console.log("Private Read Test: " + error.message);
    }
)

connTestPrivate.update({
    write: timeNow
}).then(
    function(){
        connTestPrivate.once('value').then(
            function(snapshot) {
                var privateWT = (snapshot.val() && snapshot.val().write) || 'fail';
                console.log("Private Write Test:" + privateWT);
            },
            function(error){
                console.log("Private Write Test:" + error.message);
            });
    },
    function(error){
        console.log("Private Write Test:" + error.message);
    }
);

// PROTECTED
var connTestProtected = firebase.database().ref('/connTestProtected');

connTestProtected.once('value').then(
    function(snapshot) {
        var protectedRT = (snapshot.val() && snapshot.val().read) || 'fail';
        console.log("Protected Read Test: " + protectedRT);
    },
    function(error){
        console.log("Protected Read Test: " + error.message);
    }
)

connTestProtected.update({
    write: timeNow
}).then(
    function(){
        connTestProtected.once('value').then(
            function(snapshot) {
                var protectedWT = (snapshot.val() && snapshot.val().write) || 'fail';
                console.log("Protected Write Test:" + protectedWT);
            },
            function(error){
                console.log("Protected Write Test:" + error.message);
            });
    },
    function(error){
        console.log("Protected Write Test:" + error.message);
    }
);
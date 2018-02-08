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
var connectionRef = firebase.database().ref('/testConnection');
var timeNow = Date.now();

connectionRef.set({
    readTest: "Read Successful.",
    writeTest: timeNow
});

connectionRef.once('value').then(function(snapshot) {
    var readTestResult = (snapshot.val() && snapshot.val().readTest) || 'Read Failed';
    var writeTestResult = (snapshot.val() && snapshot.val().writeTest) || 'Write Failed';
    console.log("Read Test:" + readTestResult)
    if (timeNow == writeTestResult){
        console.log("Write Test: Write Successful");
    }
});
// =============================================================================
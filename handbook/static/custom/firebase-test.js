var connectionRef = firebase.database().ref('/testConnection');
var timeNow = Date.now();
var readTestResult = "";
var writeTestResult = "";

connectionRef.set({
    readTest: "Read Successful.",
    writeTest: timeNow
});

connectionRef.once('value').then(function(snapshot) {
    readTestResult = (snapshot.val() && snapshot.val().readTest) || 'Read Failed';
    writeTestResult = (snapshot.val() && snapshot.val().writeTest) || 'Write Failed';
    console.log("Read Test:" + readTestResult)
    if (timeNow == writeTestResult){
        console.log("Write Test: Write Successful");
    }
});


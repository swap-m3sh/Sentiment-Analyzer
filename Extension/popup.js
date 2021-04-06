var checkBox=document.getElementById('filterCB');




checkBox.addEventListener('change',function(){
    // location.reload();
    if(this.checked){
        chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
            let url = tabs[0].url;
            console.log(`${url}`);

            chrome.tabs.sendMessage(tabs[0].id,{todo:'hideComments'});
            console.log('message sent');

            var notify={
                type:'basic',
                iconUrl:'Logos/youtubeLogo48.png',
                title:'Filtering Started',
                message:'Filtering process is started. Please do not close or reload this tab'
            };
            chrome.notifications.create('notification', notify,()=>{
                console.log('Notified');
            });

        });
    }

    else{
        chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
            let url = tabs[0].url;
            console.log(`${url}`);

            chrome.tabs.sendMessage(tabs[0].id,{todo:'UnHideComments'});
            console.log('unhide message sent');
        });
    }
});


// var btn=document.getElementById('filterBtn');
// btn.addEventListener('click',function(){
    
//         chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
//             let url = tabs[0].url;
//             console.log(`${url}`);

//             chrome.tabs.sendMessage(tabs[0].id,{todo:'hideComments'});
//             console.log('message sent');
//         });
    

    
// });



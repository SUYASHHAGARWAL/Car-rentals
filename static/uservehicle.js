$(document).ready(function(){

    $.getJSON("/api/test",{param:'all'},function(data){
        var htm = `<div class="rightbartemplate">
        <img src="/static/Subscription.png" width="90%" style="display: flex; margin-left: 7%; margin-top: 5%;">
</div>`
        data.map((item)=>{
            console.log(item.picture)
            htm+=`
            <div class="rightbartemplate" >
        <img src='/${item.picture}' width="45%" height="30%" style="display: flex; margin-left: 20%; margin-top: 4%;">
        <div style="margin-left: 8%; font-family: Poppins; font-size: 12; font-weight: 500; margin-top: 1%;">
        ${item.companyname}
        </div>
        <div style="margin-left: 8%; font-family: Poppins; font-size: 16; font-weight: 600;">
        ${item.subcategoryname}             
   </div>
        <div style="margin-left: 5%; font-family: Poppins; font-size: 10; font-weight: 600;">
            <img src="/static/iconDiesel.svg" width="4%" ><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.fueltype}</span>
            <img src="/static/iconTransmission.svg" width="11%" style="padding-left: 6%;"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.transmissiontype}</span>
            <img src="/static/iconSeat.svg" width="10%" style="padding-left: 5%;"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.no_of_seats} Seats</span>
        </div>
        <div style="margin-left: 8%;">
            <div style="font-size: 26px; margin-top: 4%; display: flex; justify-content: space-between;">
                <div style="display: flex; margin-left: 1%; margin-top: 1%; ">
                    &#8377<span style="font-family: Poppins; font-size: 26px; font-weight: 700;">
                    ${item.price}
                    </span>
                </div>
                <div class="button_style" style="display: flex; margin-right: 7%; margin-top: 1%;">

                <a href='/api/displayvehiclelist/?vehicles=${JSON.stringify(item)}' style="text-decoration: none; cursor:pointer; color: #000;">
                    <div style="display: flex; align-items: center; font-size: 15; color: #fff; font-weight: bold;">Book  ></div>
                </div></a>
            </div>
        </div>
        <div style="margin-left: 5%; font-family: Poppins; font-size: 12; font-weight: 500; margin-top: 5%;">
            288 kms | Price <b>exclude</b> fuel cost 
        </div>
    </div>`
        })


        $('#listvehicle').html(htm)

    });

    function searching(value){
        console.log(value)
        $.getJSON("/api/test",{param:value},function(data){
            var htm = `<div class="rightbartemplate">
            <img src="/static/Subscription.png" width="90%" style="display: flex; margin-left: 7%; margin-top: 5%;">
    </div>`
    console.log(data)
            data.map((item)=>{
                 htm+=`
                 <div class="rightbartemplate" style="margin-left: 3%;" onclick="window.location.href='/api/threeindex'">
                 <img src='/${item.picture}' width="45%" height="30%" style="display: flex; margin-left: 20%; margin-top: 4%;">
                 <div style="margin-left: 8%; font-family: Poppins; font-size: 12; font-weight: 500; margin-top: 1%;">
                 ${item.companyname}
                 </div>
                 <div style="margin-left: 8%; font-family: Poppins; font-size: 16; font-weight: 600;">
                 ${item.subcategoryname}             
            </div>
                 <div style="margin-left: 5%; font-family: Poppins; font-size: 10; font-weight: 600;">
                     <img src="/static/iconDiesel.svg" width="4%" ><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.fueltype}</span>
                     <img src="/static/iconTransmission.svg" width="11%" style="padding-left: 6%;"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.transmissiontype}</span>
                     <img src="/static/iconSeat.svg" width="10%" style="padding-left: 5%;"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.no_of_seats} Seats</span>
                 </div>
                 <div style="margin-left: 8%;">
                     <div style="font-size: 26px; margin-top: 4%; display: flex; justify-content: space-between;">
                         <div style="display: flex; margin-left: 1%; margin-top: 1%; ">
                             &#8377<span style="font-family: Poppins; font-size: 26px; font-weight: 700;">
                             ${item.price}
                             </span>
                         </div>
                         <div class="button_style" style="display: flex; margin-right: 7%; margin-top: 1%;">

                         <a href='/api/displayvehiclelist/?vehicles=${JSON.stringify(item)}' style="text-decoration: none; cursor:pointer; color: #000;" >
                             <div style="display: flex; align-items: center; font-size: 15; color: #fff; font-weight: bold;">Book  ></div>
                         </div></a>
                     </div>
                 </div>
                 <div style="margin-left: 5%; font-family: Poppins; font-size: 12; font-weight: 500; margin-top: 5%;">
                     288 kms | Price <b>exclude</b> fuel cost 
                 </div>
             </div>`
            })
        
        $('#listvehicle').html(htm)

    });
    }
    // $('.city').click(function(){
    //     var sb=''
    //     $('.city').map(function(i,item){
    //       if($(this).prop("checked")) 
    //       {sb+="'"+($(this).val())+"' ,"}
    //     });
    //     sb=sb.substring(0,sb.length-1)
    //     if(sb=='')
    //         searching('all')
    //     else
    //         searching(sb)
    // })
    var p=[]
    let sb=''
    let sf=''
    $('.brand').click(function(){
        sb=''

        $('.brand').map(function(i,item){
          if($(this).prop("checked")) 
             {sb+="'"+($(this).val())+"' ,"}
            p.push($(this).val())
          //console.log(sb)
          });
          
          sb=sb.substring(0,sb.length-1)
          sb = sb+sf
        //  console.log(p)
          console.log(sb)
        // p.push(sb)
        // if(sb=='')
        //     searching('all')
        // else
        //     searching(sb)
        if(sb=='')
            searching('all')
        else
            searching(sb)
    })
    $('.fuel').click(function(){
        sf=''
        $('.fuel').map(function(i,item){
          if($(this).prop("checked")) 
          {sf+="'"+($(this).val())+"' ,"}
        });
        sf=sf.substring(0,sf.length-1)
        sb+=sf
        console.log(sb)
        p.push(sf)
        if(sb=='')
            searching('all')
        else
            searching(sb)
    })
})
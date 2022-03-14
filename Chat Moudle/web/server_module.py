
const net = require("net")

const chatServer = net.createServer()

let clientMap = {} 

let i = 0


chatServer.on("connection",(client)=>{
    client.name = ++i;
    clientMap[client.name] = client;


    client.on("data",message=>{

        boardcast(client,message)
        
    })


    client.on("error",()=>{
        console.log(client.name + "下机了")
    })


})


function boardcast(client,message){
    for(var key in clientMap){
        clientMap[key].write("\n" + client.name + "说" + message)
    }
}

chatServer.listen(9000)

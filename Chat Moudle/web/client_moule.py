const net = require("net")
const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const client = new net.Socket()

client.connect(9000,"localhost",()=>{
    client.write("hello")
})


client.on("data",message=>{
    console.log(message.toString())
    say()
})

function say(){
    rl.question("content：",(str)=>{
        client.write(str)
    })
}

client.on("error",()=>{
    console.log("error")
})

import Product from "./product";
function ProductTab(){
    let option=["Hi-tech", "Durable", "Fast"];
    let option2={a: "hi-tech", b: "durable",c: "fast"};
    let style= {
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "center",
        alignItems: "center"

    };
    return (
        <div style={style}>
        {/* <Product title="Tab" price={2722} />
        <Product title="laptop" price={5050}/>
        <Product title="car" price={2758}/> */}
        <Product title="Mack Book A2" idx={0}/>
        <Product title="Apple 12 Pro" idx={1}/>
        <Product title="Boat Rock Z2" idx={2}/>
        <Product title="Apple 15 Pro" idx={3}/>

        </div>
    );
}
export default ProductTab;




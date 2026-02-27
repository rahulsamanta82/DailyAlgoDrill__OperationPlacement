import "./product.css"
import Price from "./price";
function Product({ title, idx }) {
    // let isDiscount=price>3000 ? "5%" : "";
    // let abc={ backgroundColor: isDiscount ? "green" : "pink"};
    let oldPrice=["1205","2507","8250","3692"]
    let newPrice=["5800","8769","4658","7562"]
    let des=[
        ["A2 for coding","And design"],
        ["More Storage","For Security"],
        ["Best Sound","Or battery"],
        ["For Camara","And Storage"]
    ]
    return (
        <div className="Product">
            {/* <h2>{title}</h2>
            <h5>Price:{price}</h5>
            {price>3000 && <p>Discount of 5%</p>} */}
            {/* <p>Products</p> */}
            <h1>{title}</h1>
            <p>Title</p>
            <p>{des[idx][0]}</p>
            <p>{des[idx][1]}</p>
            <Price oldPrice={oldPrice[idx]} newPrice={newPrice[idx]} />
        </div>

    );

}

export default Product;




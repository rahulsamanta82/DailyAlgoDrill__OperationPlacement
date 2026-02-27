export default function Price({ oldPrice, newPrice }) {
    let oldStyle={
        textDecorationLine: "line-through"
    }
    let newStyle={
        fontWeight: "bold"
    }
    let bg={
        backgroundColor: "#e0c367",
        height: "30px",
        width: "250px",
        borderBottomLeftRadius: "14px",
        borderBottomRightRadius: "14px",
        
    }
    return (
        <div style={bg}>
            <span style={oldStyle}>{oldPrice}</span>
            &nbsp; &nbsp;
            <span style={newStyle}>{newPrice}</span>
        </div>

    );
}


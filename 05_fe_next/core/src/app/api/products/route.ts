import { NextRequest, NextResponse } from "next/server";
import ProductSchema from "./schema";

const products = [
  {
    id: 1,
    name: "Milk",
    price: 3.5,
  },
  {
    id: 2,
    name: "Bread",
    price: 1.5,
  },
];

export function GET(request: NextRequest) {
  return NextResponse.json(products, { status: 200 });
}

export async function POST(request: NextRequest) {
  let data;
  try {
    data = await request.json();
  } catch (error) {
    return NextResponse.json(
      { error: "Invalid or missing JSON body" },
      { status: 400 }
    );
  }

  const validatedData = ProductSchema.safeParse(data);
  if (!validatedData.success)
    return NextResponse.json(validatedData.error.errors, { status: 400 });
  return NextResponse.json(
    {
      id: 1,
      name: validatedData.data.name,
      price: validatedData.data.price,
    },
    { status: 201 }
  );
}

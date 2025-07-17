"use client"
import React, { useState } from 'react'
import { useForm } from "react-hook-form";
import { zodResolver } from '@hookform/resolvers/zod';
import {z} from "zod"
import { signIn } from 'next-auth/react';
import { useRouter } from 'next/navigation';

const LoginSchema = z.object({
    email: z.string().email(),
    password: z.string().min(3)
})

type Login = z.infer<typeof LoginSchema>



const LoginPage = () => {
    const router = useRouter()
    const [error, setError] = useState("")
    const [loading, isLoading] = useState(false)
    const {register, handleSubmit, formState: {errors}} = useForm<Login>({resolver: zodResolver(LoginSchema)})

    const onSubmit = async (data: Login)=>{
        console.log(data);
        isLoading(true)
        const response = await signIn("credentials", {
            ...data,
            redirect: false
        })
        console.log("hkjhjkhkjjhk", response)
        if (response?.ok === true){
            router.push("/")
        }else if(response?.error){
            isLoading(false)
            setError(response.error)
        }
    }
  return (
    <>
    {error && <p className='text-red-600'>{error}</p>}
    <form className='p-5 space-x-3' onSubmit={handleSubmit(onSubmit)}>
        <input type="text" className='border p-2' {...register("email")} />
        {errors.email && <p>{errors.email.message}</p>}
        <input type="password" className='border p-2' {...register("password")} />
        {errors.password && <p>{errors.password.message}</p>}
        <button 
        type="submit" 
        className='text-white bg-blue-700 hover:bg-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2'
        disabled={loading}
        >
        Submit {loading && <span>Loading....</span>}</button>
    </form>
    </>
  )
}

export default LoginPage
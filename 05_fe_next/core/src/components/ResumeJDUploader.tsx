'use client'

import { useState } from 'react'
import axios from '@/utils/api'
import MatchResult from './ResponseJD'

interface ResponseData{
  description: string; 
  score: number 
}

export default function ResumeJDUploader() {
  const [resume, setResume] = useState<File | null>(null)
  const [jd, setJd] = useState<File | null>(null)
  const [loading, setLoading] = useState(false)
  const [response, setResponse] = useState<ResponseData>()

  const handleUpload = async () => {
    if (!resume || !jd) return alert("Please upload both files")

    const formData = new FormData()
    formData.append("resume", resume)
    formData.append("job_description", jd)

    try {
      setLoading(true)
      const res = await axios.post('/compare', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      setResponse(res.data)
    } catch (err) {
      alert("Upload failed")
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <div className="p-8 max-w-4xl mx-auto">
        <h2 className="text-2xl font-semibold mb-6 text-center">Upload Resume & Job Description</h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="flex flex-col items-start">
            <label className="mb-2 font-medium">Upload Resume (.pdf)</label>
            <input
              type="file"
              accept=".pdf"
              onChange={(e) => setResume(e.target.files?.[0] || null)}
              className="border p-2 rounded w-full"
            />
          </div>

          <div className="flex flex-col items-start">
            <label className="mb-2 font-medium">Upload Job Description (.txt)</label>
            <input
              type="file"
              accept=".txt"
              onChange={(e) => setJd(e.target.files?.[0] || null)}
              className="border p-2 rounded w-full"
            />
          </div>
        </div>

        <div className="mt-6 text-center">
          <button
            onClick={handleUpload}
            disabled={loading}
            className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
          >
            {loading ? "Uploading..." : "Submit"}
          </button>
        </div>
      </div>
      { response &&
      <div>
        <MatchResult result={response} />
      </div>
      }
    </>
  )
}

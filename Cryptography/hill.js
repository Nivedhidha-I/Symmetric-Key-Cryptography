var lock = [
	[1, -2, 2],
	[-1, 1, 3],
	[1, -1, -4],
];

// Matrix Multiplication of key/lock with
function matrixmultiply(m1, m2) {
	var m3 = [];
	var x = m1.length;
	var y = m2[0].length;
	var z = m1[0].length;
	for (i = 0; i < x; i++) {
		m3.push([]);
		for (j = 0; j < y; j++) {
			m3[i][j] = 0;
			for (k = 0; k < z; k++) {
				m3[i][j] += m1[i][k] * m2[k][j];
			}
		}
	}
	return m3;
}

// used for finding the cofactor matrix (used in inverse)
function cofactor(matrix) {
	var cofactor = [];
	for (i = 0; i < matrix.length; i++) {
		cofactor.push([]);
		for (j = 0; j < matrix[0].length; j++) {
			var minormat = [];
			var x = 0,
				y = 0;
			// creating minor matrix for each element matrix[i][j]
			for (k = 0; k < matrix.length; k++) {
				minormat.push([]);
				for (l = 0; l < matrix[0].length; l++) {
					if (k != i && l != j) {
						minormat[x][y] = matrix[k][l];
						y++;
					}
				}
				y = 0;
				if (k < matrix.length - 1) {
					x++;
				}
			}
			minormat.splice(i, 1);

			// finding minor and cofactor of matrix
			var det =
				minormat[0][0] * minormat[1][1] -
				minormat[0][1] * minormat[1][0];
			if ((i + j) % 2 == 1) cofactor[i][j] = -det;
			else cofactor[i][j] = det;
		}
	}
	return cofactor;
}

// Function to find the inverse of key
function matrixinverse(m) {
	// find det(m)
	var det =
		m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
		m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
		m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]);

	// finding cofactor matrix
	var adj = cofactor(m);

	// find adjoint matrix (transpose of cofactor) & find inverse by multiplying 1/det(m) and adj(m)
	var inverse = [];
	for (i = 0; i < adj.length; i++) {
		inverse.push([]);
		for (j = 0; j < adj.length; j++) {
			inverse[i][j] = adj[j][i] / det;
		}
	}
	return inverse;
}

// Function for Encryption of Message input
function encrypt() {
	// get input from user
	var message = document.getElementById('encryption').value;

	// converting to upper case
	text = message.toString().toUpperCase();
	var values = [];
	var k = 0;

	// First converting the given text into numbers
	for (var i = 0; i < text.length; i++) {
		char = text.charCodeAt(i);
		if (char == 32) {
			values[k] = 0;
			k++;
		} else if ((char >= 65) & (char <= 90)) {
			values[k] = char - 64;
			k++;
		}
	}

	// converting values into a matrix (row x lock.length)
	var twodarr = [];
	var row = Math.ceil(values.length / lock.length);
	k = 0;
	for (i = 0; i < row; i++) {
		twodarr.push([]);
		for (j = 0; j < lock.length; j++) {
			if (k < values.length) twodarr[i][j] = values[k];
			else twodarr[i][j] = 0;
			k++;
		}
	}

	// Locking Matrix (encryption)
	var mul = matrixmultiply(twodarr, lock);

	// array is converted into a string for printing
	var encrypted = [];
	k = 0;
	for (i = 0; i < mul.length; i++) {
		for (j = 0; j < mul[0].length; j++) {
			encrypted[k] = mul[i][j];
			k++;
		}
	}
	document.getElementById('encrypted').innerHTML = encrypted;
	decrypt(encrypted);
}

// Fuction for Decryption of Encoded message
function decrypt(encrypt) {
	// converting one d array into a matrix (row x lock.length)
	var twodarr = [];
	var row = Math.ceil(encrypt.length / lock.length);
	k = 0;
	for (i = 0; i < row; i++) {
		twodarr.push([]);
		for (j = 0; j < lock.length; j++) {
			if (k < encrypt.length) twodarr[i][j] = encrypt[k];
			else twodarr[i][j] = 0;
			k++;
		}
	}

	// finding key for lock (inverse of lock)
	var key = matrixinverse(lock);

	// Multiplying key with encoded message (decryptions)
	var mul = matrixmultiply(twodarr, key);

	// convert two d array to one d array
	var onedarr = [];
	k = 0;
	for (i = 0; i < mul.length; i++) {
		for (j = 0; j < mul[0].length; j++) {
			onedarr[k] = mul[i][j];
			k++;
		}
	}

	// converting the matrix[0-26] into respective ascii matrix
	for (var i = 0; i < onedarr.length; i++) {
		char = onedarr[i];
		if (char == 0) onedarr[i] = 32;
		else if ((char >= 1) & (char <= 26)) onedarr[i] = char + 64;
	}

	// converting ascii matrix into respective charaters
	for (var i = 0; i < onedarr.length; i++)
		onedarr[i] = String.fromCharCode(onedarr[i]);
	// Joining into string and returning the result
	var decrypted = onedarr.join('');
	document.getElementById('decrypted').innerHTML = decrypted;
}
